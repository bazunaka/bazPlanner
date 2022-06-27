using System;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using static bazPlannerWPF.Owner;


namespace bazPlannerWPF
{
    /// <summary>
    /// Логика взаимодействия для create_user.xaml
    /// </summary>
    public partial class create_user : Window
    {
        public create_user()
        {
            InitializeComponent();
        }

        Owner newUser = new Owner();
        public String asd = newUser.nameOwner;
    }
}
