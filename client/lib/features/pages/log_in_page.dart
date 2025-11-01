import 'package:client/core/theme/app_pallete.dart';
import 'package:client/core/widget/custom_field.dart';
import 'package:client/features/widget/auth_widget_button.dart';
import 'package:flutter/material.dart';

class LogInPage extends StatefulWidget {
  const LogInPage({super.key});

  @override
  State<LogInPage> createState() => _LogInPageState();
}

class _LogInPageState extends State<LogInPage> {
  final nameController = TextEditingController();
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  final formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Padding(
        padding: EdgeInsets.all(32),
        child: Form(
          key: formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Sign In.',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 50),
              ),
              SizedBox(height: 20),
              CustomField(hintText: 'Email', controller: emailController),
              SizedBox(height: 15),
              CustomField(
                hintText: 'Password',
                controller: passwordController,
                isObscureText: true,
              ),
              SizedBox(height: 20),
              AuthWidgetButton(buttonText: 'Sign In', onTap: () {}),
              SizedBox(height: 20),
              RichText(
                text: TextSpan(
                  text: 'Create an account? ',
                  style: Theme.of(context).textTheme.titleMedium,
                  children: const [
                    TextSpan(
                      text: 'Sign Up',
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 17,
                        color: Pallete.gradient2,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
