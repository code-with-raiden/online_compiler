from django.shortcuts import render
from django.http import HttpResponse
from .forms import CodeForm
import subprocess

def compile_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            inputs = form.cleaned_data.get('inputs', '')
            
            # Write the user's code to a file
            with open('temp_code.py', 'w') as file:
                file.write(code)
            
            # Execute the code
            try:
                result = subprocess.run(
                    ['python', 'temp_code.py'],
                    capture_output=True,
                    text=True,
                    input=inputs,  # Provide the inputs to the subprocess
                    timeout=10  # Add timeout to avoid hanging
                )
                output = result.stdout + result.stderr
            except subprocess.CalledProcessError as e:
                output = str(e)
            except Exception as e:
                output = str(e)

            # Handle the edit old code request
            if 'edit_old_code' in request.POST:
                form = CodeForm(initial={'code': request.POST.get('code'), 'inputs': request.POST.get('inputs')})
                return render(request, 'compiler/compile.html', {'form': form})

            return render(request, 'compiler/result.html', {'output': output, 'form': form})
    else:
        form = CodeForm()
    return render(request, 'compiler/compile.html', {'form': form})
