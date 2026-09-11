from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='582ac975-495c-5a5a-9d71-762b5b892778',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name',
    display_name='Piplup',
    searchable_by=['Piplup', 'Basic', 'Piplup'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=393,
    abilities=[
        Attack(
            title='Splatter',
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
