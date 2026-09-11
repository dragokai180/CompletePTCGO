from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ca7686b-d67d-5292-8bdf-3bc4d7e8fbd5',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGX.Name',
    display_name='Naganadel-GX',
    searchable_by=['Naganadel-GX', 'Stage 1', 'GX', 'Ultra Beast', 'NaganadelGX'],
    subtypes=['Stage 1', 'GX', 'Ultra Beast'],
    collector_number=160,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name',
    family_id=803,
    abilities=[
        Ability(
            title='Ultra Conversion',
            game_text='Once during your turn (before your attack), you may discard an Ultra Beast card from your hand. If you do, draw 3 cards.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Venom Shot',
            game_text="Discard 2 Energy from this Pokémon. This attack does 170 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
        Attack(
            title='Injection-GX',
            game_text="Add a card from your opponent's discard pile to their Prize cards face down. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
