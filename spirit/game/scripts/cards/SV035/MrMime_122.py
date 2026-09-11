from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='12d211bd-ca32-5eda-a78d-dbeca413377e',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name',
    display_name='Mr. Mime',
    searchable_by=['Mr. Mime', 'Basic', 'MrMime'],
    subtypes=['Basic'],
    collector_number=122,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=122,
    abilities=[
        Ability(
            title='Mimic Barrier',
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon.",
            passive=standard_passive("If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon."),
        ),
        Attack(
            title='Psypower',
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
