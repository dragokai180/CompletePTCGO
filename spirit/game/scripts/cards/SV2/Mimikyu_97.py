from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f9c25ebe-fabc-591a-bffb-56e0c1bce199',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name',
    display_name='Mimikyu',
    searchable_by=['Mimikyu', 'Basic', 'Mimikyu'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=778,
    abilities=[
        Ability(
            title='Safeguard',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex and Pokémon V.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex and Pokémon V."),
        ),
        Attack(
            title='Ghost Eye',
            game_text="Put 7 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
