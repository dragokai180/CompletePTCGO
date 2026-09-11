from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6adbc698-1490-5529-859b-fa1aa1ff5e2c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramCharizardGX.Name',
    display_name='Reshiram & Charizard-GX',
    searchable_by=['Reshiram & Charizard-GX', 'Basic', 'TAG TEAM', 'GX', 'ReshiramCharizardGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=201,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=6,
    abilities=[
        Attack(
            title='Outrage',
            game_text='This attack does 10 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Flare Strike',
            game_text="This Pokémon can't use Flare Strike during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Double Blaze-GX',
            game_text="If this Pokémon has at least 3 extra Fire Energy attached to it (in addition to this attack's cost), this attack does 100 more damage, and this attack's damage isn't affected by any effects on your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 3},
            damage=200,
            damage_operator='+',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
