from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d3b1944-7b58-5d3c-b01e-24093d7dc220',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MagcargoGX.Name',
    display_name='Magcargo-GX',
    searchable_by=['Magcargo-GX', 'Stage 1', 'GX', 'MagcargoGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=44,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name',
    family_id=218,
    abilities=[
        Ability(
            title='Crushing Charge',
            game_text="Once during your turn (before your attack), you may discard the top card of your deck. If it's a basic Energy card, attach it to 1 of your Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Lava Flow',
            game_text='Discard any amount of basic Energy from this Pokémon. This attack does 50 more damage for each card you discarded in this way.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Burning Magma-GX',
            game_text="Discard the top 5 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
