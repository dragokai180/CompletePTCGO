from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e180907-91ac-5b99-b9a8-ca528a8c7b77',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasNumel.Name',
    display_name="Team Magma's Numel",
    searchable_by=["Team Magma's Numel", 'Basic', 'TeamMagmasNumel'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=322,
    abilities=[
        Attack(
            title='Ember',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
