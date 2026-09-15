from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='639c044e-5b35-5a3a-9091-9c24562ead30',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozmaGX.Name',
    display_name='Dawn Wings Necrozma-GX',
    searchable_by=['Dawn Wings Necrozma-GX', 'Basic', 'GX', 'Ultra Beast', 'DawnWingsNecrozmaGX'],
    subtypes=['Basic', 'GX', 'Ultra Beast'],
    collector_number=101,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=800,
    abilities=[
        Ability(
            title='Invasion',
            game_text='Once during your turn (before your attack), if this Pokémon is on your Bench, you may switch it with your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Dark Flash',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title="Moon's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=180,
            effect=standard_attack,
            locks_next_turn=False,
            gx=True,
        ),
    ],
)
