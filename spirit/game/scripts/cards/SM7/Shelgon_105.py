from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7d1b9d4b-079b-5330-91ad-ad8e7e3f401e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name',
    display_name='Shelgon',
    searchable_by=['Shelgon', 'Stage 1', 'Shelgon'],
    subtypes=['Stage 1'],
    collector_number=105,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name',
    family_id=371,
    abilities=[
        Attack(
            title='Raging Blade',
            game_text='If this Pokémon has any damage counters on it, this attack does 50 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
