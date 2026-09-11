from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e1d9b45e-cd50-5126-abdb-0ac5d152b5f5',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MagearnaEX.Name',
    display_name='Magearna-EX',
    searchable_by=['Magearna-EX', 'Basic', 'EX', 'MagearnaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=75,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=801,
    abilities=[
        Ability(
            title='Mystic Heart',
            game_text="Prevent all effects of your opponent's attacks, except damage, done to each of your Pokémon that has any Metal Energy attached to it. (Existing effects are not removed.)",
            passive=standard_passive("Prevent all effects of your opponent's attacks, except damage, done to each of your Pokémon that has any Metal Energy attached to it. (Existing effects are not removed.)"),
        ),
        Attack(
            title='Soul Blaster',
            game_text="During your next turn, this Pokémon's Soul Blaster attack's base damage is 60.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
