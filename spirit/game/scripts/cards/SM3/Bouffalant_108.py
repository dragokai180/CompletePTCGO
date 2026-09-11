from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c1ddc55c-f9a6-525b-a50a-a808e9e0e1d6',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name',
    display_name='Bouffalant',
    searchable_by=['Bouffalant', 'Basic', 'Bouffalant'],
    subtypes=['Basic'],
    collector_number=108,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=626,
    abilities=[
        Attack(
            title='Bouffant Head',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Knock Over',
            game_text='You may discard any Stadium card in play.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
