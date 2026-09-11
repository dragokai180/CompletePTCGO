from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4cd323ee-f2e4-5da6-a957-773c974536a0',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name',
    display_name='Porygon-Z',
    searchable_by=['Porygon-Z', 'Stage 2', 'PorygonZ'],
    subtypes=['Stage 2'],
    collector_number=144,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    family_id=137,
    abilities=[
        Ability(
            title='Buggy Turbo',
            game_text='Once during your turn, you may flip a coin. If heads, attach up to 4 Basic Energy cards from your discard pile to this Pokémon. If tails, discard an Energy from this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Energized Attack',
            game_text='This attack does 40 damage for each Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
