from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1a35beb6-44ca-5af8-9158-4487a85afaec',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name',
    display_name='Prinplup',
    searchable_by=['Prinplup', 'Stage 1', 'Prinplup'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name',
    family_id=393,
    abilities=[
        Attack(
            title='Water Drip',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Direct Dive',
            game_text="Discard all Energy from this Pokémon. This attack does 100 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3},
            effect=standard_attack,
        ),
    ],
)
