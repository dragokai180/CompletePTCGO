from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3db6faa8-68fa-5d77-a1c4-ebbc893a390f',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AurorusEX.Name',
    display_name='Aurorus-EX',
    searchable_by=['Aurorus-EX', 'Basic', 'EX', 'AurorusEX'],
    subtypes=['Basic', 'EX'],
    collector_number=102,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=699,
    abilities=[
        Ability(
            title='Frozen Charm',
            game_text="Each of your Pokémon that has any Water Energy attached to it can't be Paralyzed. (If any of those Pokémon are Paralyzed, remove that Special Condition.)",
            passive=standard_passive("Each of your Pokémon that has any Water Energy attached to it can't be Paralyzed. (If any of those Pokémon are Paralyzed, remove that Special Condition.)"),
        ),
        Attack(
            title='Crystal Breath',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
