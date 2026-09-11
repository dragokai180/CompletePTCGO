from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='411ab3d7-ad26-50ea-8877-83edc7e8a53f',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name',
    display_name='Lombre',
    searchable_by=['Lombre', 'Stage 1', 'Lombre'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name',
    family_id=270,
    abilities=[
        Ability(
            title='Aqua Lift',
            game_text='If this Pokémon has any Water Energy attached to it, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Water Energy attached to it, it has no Retreat Cost.'),
        ),
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
