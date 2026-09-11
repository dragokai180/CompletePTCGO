from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a196ea2-1d25-5a3a-a9a5-d18bc8146e2d',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasCamerupt.Name',
    display_name="Team Magma's Camerupt",
    searchable_by=["Team Magma's Camerupt", 'Stage 1', 'TeamMagmasCamerupt'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasNumel.Name',
    family_id=322,
    abilities=[
        Ability(
            title='Burning Draft',
            game_text='Once during your turn (before your attack), you may attach a Fighting or Fire Energy card from your discard pile to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Flame Ball',
            game_text='Move a basic Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
