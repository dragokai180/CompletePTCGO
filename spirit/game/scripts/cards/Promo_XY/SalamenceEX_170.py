from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='835dbd0a-fe86-5cbe-beab-976a8e690a53',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceEX.Name',
    display_name='Salamence-EX',
    searchable_by=['Salamence-EX', 'Basic', 'EX', 'SalamenceEX'],
    subtypes=['Basic', 'EX'],
    collector_number=170,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=373,
    abilities=[
        Attack(
            title='Beastly Fang',
            game_text="This attack does 50 more damage for each of your opponent's Pokémon-EX.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Strike',
            game_text="This Pokémon can't use Dragon Strike during your next turn.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
