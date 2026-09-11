from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a4af434-c6b0-56aa-ba20-f767a02a4688',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoGX.Name',
    display_name='Mewtwo-GX',
    searchable_by=['Mewtwo-GX', 'Basic', 'GX', 'MewtwoGX'],
    subtypes=['Basic', 'GX'],
    collector_number=196,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Attack(
            title='Telekinesis',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Reigning Pulse',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Psychic Nova-GX',
            game_text="Prevent all damage done to this Pokémon by attacks during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=standard_attack,
            locks_next_turn=True,
            gx=True,
        ),
    ],
)
