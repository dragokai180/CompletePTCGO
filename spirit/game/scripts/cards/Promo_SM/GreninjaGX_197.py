from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='22356117-cc47-58bb-a78e-59026305aa46',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaGX.Name',
    display_name='Greninja-GX',
    searchable_by=['Greninja-GX', 'Stage 2', 'GX', 'GreninjaGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=197,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=658,
    abilities=[
        Ability(
            title='Elusive Master',
            game_text='Once during your turn (before your attack), if this Pokémon is the last card in your hand, you may play it onto your Bench. If you do, draw 3 cards.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
            usable_from='hand',
        ),
        Attack(
            title='Mist Slash',
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
        Attack(
            title='Dark Mist-GX',
            game_text="Put 1 of your opponent's Benched Pokémon and all cards attached to it into your opponent's hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
