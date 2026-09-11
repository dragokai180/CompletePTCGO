from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8a49fc1b-23a3-53e6-8763-6d0238da3fe3',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossGX.Name',
    display_name='Metagross-GX',
    searchable_by=['Metagross-GX', 'Stage 2', 'GX', 'MetagrossGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=85,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    family_id=374,
    abilities=[
        Ability(
            title='Geotech System',
            game_text='Once during your turn (before your attack), you may attach a Psychic or Metal Energy card from your discard pile to your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Giga Hammer',
            game_text="This Pokémon can't use Giga Hammer during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Algorithm-GX',
            game_text="Search your deck for up to 5 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
