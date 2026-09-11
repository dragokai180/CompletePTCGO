from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a016454f-7b7f-5a5f-ab91-a12dd9cabe05',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DecidueyeGX.Name',
    display_name='Decidueye-GX',
    searchable_by=['Decidueye-GX', 'Stage 2', 'GX', 'DecidueyeGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=12,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name',
    family_id=722,
    abilities=[
        Ability(
            title='Feather Arrow',
            game_text="Once during your turn (before your attack), you may put 2 damage counters on 1 of your opponent's Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
        Attack(
            title='Hollow Hunt-GX',
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
