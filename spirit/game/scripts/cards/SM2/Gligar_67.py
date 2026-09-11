from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0768f8ee-51a2-52df-b182-32e0e685e729',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    display_name='Gligar',
    searchable_by=['Gligar', 'Basic', 'Gligar'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=207,
    abilities=[
        Attack(
            title='Double Shot',
            game_text="This attack does 10 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
    ],
)
