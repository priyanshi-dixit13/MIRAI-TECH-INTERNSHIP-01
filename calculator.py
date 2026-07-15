import streamlit as st

st.title("Basic calculator")
st.write("Enter two numbers and select any operation")

num1 = st.number_input("Enter first number",value=0.0)
num2 = st.number_input("Enter second number",value=0.0)

operation = st.selectionbox(
    "Choose operation",
    ["Addition","Subtraction","Multiplication","Division"]
)

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result:{result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result:{result}")

    elif operation ==  "Multiplication":
        result = num1 * num2
        st.success(f"Result:{result}")

    elif operation == "Division":
        if num2 ==0:
            st.error("Division by zero is not allowed.")    

    else:
        result = num1 / num2
        st.success(f"Result:{result}")
    


