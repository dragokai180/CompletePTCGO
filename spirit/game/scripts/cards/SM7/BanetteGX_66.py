from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eef613b6-2b1c-59f3-a3ee-84b9c0387986',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BanetteGX.Name',
    display_name='Banette-GX',
    searchable_by=['Banette-GX', 'Stage 1', 'GX', 'BanetteGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=66,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    family_id=353,
    abilities=[
        Ability(
            title='Shady Move',
            game_text='Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may move 1 damage counter from 1 Pokémon to another Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Shadow Chant',
            game_text="This attack does 10 more damage for each Supporter card in your discard pile. You can't add more than 100 damage in this way.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Tomb Hunt-GX',
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
