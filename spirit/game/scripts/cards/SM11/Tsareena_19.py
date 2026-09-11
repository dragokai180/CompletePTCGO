from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ae08eac-b8a1-5805-967c-fe142014a11c',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name',
    display_name='Tsareena',
    searchable_by=['Tsareena', 'Stage 2', 'Tsareena'],
    subtypes=['Stage 2'],
    collector_number=19,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    family_id=761,
    abilities=[
        Ability(
            title='Queenly Reward',
            game_text='Once during your turn (before your attack), you may attach a Grass Energy card from your discard pile to your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='High Jump Kick',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
