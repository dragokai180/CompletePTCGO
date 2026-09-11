from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd9d9c7c-6d5f-5537-b8b1-178ccd61630f',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name',
    display_name='Regirock',
    searchable_by=['Regirock', 'Basic', 'Regirock'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=377,
    abilities=[
        Ability(
            title='Rock Peak Growl',
            game_text="Your Registeel's attacks do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("Your Registeel's attacks do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Tough Swing',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
