using System;
using System.Windows;
using static bazPlannerWPF.Owner;
using static bazPlannerWPF.Project;

namespace bazPlannerWPF
{
    public partial class auth : Window
    {
        public auth()
        {
            InitializeComponent();
        }

        private void AuthToDB(object sender, RoutedEventArgs e)
        {
            ((MainWindow)Application.Current.MainWindow).labelAuth.Content =  Auth(TextBoxUser.Text, TextBoxPassword.Text);
            SelectProject();
            //((MainWindow)Application.Current.MainWindow).listElements.Items.Add(SelectProject());
            Close();
        }
    }
}