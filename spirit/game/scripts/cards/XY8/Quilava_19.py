from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bdd098ab-3300-53f9-9630-1d80bd32955f',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name',
    display_name='Quilava',
    searchable_by=['Quilava', 'Stage 1', 'Quilava'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name',
    family_id=155,
    abilities=[
        Attack(
            title='Mini Eruption',
            game_text='Discard the top card of your deck. If that card is an Energy card, this attack does 30 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
