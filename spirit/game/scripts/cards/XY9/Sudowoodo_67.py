from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37ca15b6-e223-56c7-8d1b-b456d276642b',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name',
    display_name='Sudowoodo',
    searchable_by=['Sudowoodo', 'Basic', 'Sudowoodo'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=185,
    abilities=[
        Attack(
            title='Watch and Learn',
            game_text="If your opponent's Pokémon used an attack during his or her last turn, use it as this attack.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
