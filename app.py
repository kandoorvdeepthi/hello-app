def greet(name: str) -> str:
  "return greeting for the given name."
  name = name.strip()
  if not name:
    raise ValueError('Name cannot be empty')
  return f"Hello {name}"

def main():
  while True:
    try:
      name = input('enter your name:')
      print(greet(name))
      break
    except ValueError as error:
      print(f'Error {error}. Please try again.')
    except(KeyboardInterrupt, EOFError):
      print('\nGoodbye')
      break

if __name__ == "__main__":
    main()


#ValueError happens when a value is the right type but makes no sense
#KeyboardInterrupt happens when the user presses Ctrl+C while the program is running.
#EOFError means “End Of File Error.” It happens when input() is waiting for text but the input stream closes, so there’s nothing left to read.