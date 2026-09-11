from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70be3724-5c22-57f9-81ee-932975cd9864',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name',
    display_name='Minior',
    searchable_by=['Minior', 'Basic', 'Minior'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=774,
    abilities=[
        Attack(
            title='Swift',
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Cosmicsplosion',
            game_text='This Pokémon is Knocked Out.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
