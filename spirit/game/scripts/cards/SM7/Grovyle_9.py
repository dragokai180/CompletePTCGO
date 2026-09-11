from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='98a8163c-f550-5c01-8023-909a90b4f2ef',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name',
    display_name='Grovyle',
    searchable_by=['Grovyle', 'Stage 1', 'Grovyle'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name',
    family_id=252,
    abilities=[
        Attack(
            title='Leaf Blade',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
