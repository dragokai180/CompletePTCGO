from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f2dd9d3-f2bf-5261-a039-a54856d2b2a6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TingLuex.Name',
    display_name='Ting-Lu ex',
    searchable_by=['Ting-Lu ex', 'Basic', 'ex', 'TingLuex'],
    subtypes=['Basic', 'ex'],
    collector_number=127,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=1003,
    abilities=[
        Ability(
            title='Cursed Land',
            game_text="As long as this Pokémon is in the Active Spot, your opponent's Pokémon in play that have any damage counters on them have no Abilities, except for Pokémon ex.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, your opponent's Pokémon in play that have any damage counters on them have no Abilities, except for Pokémon ex."),
        ),
        Attack(
            title='Land Scoop',
            game_text="Put 2 damage counters on 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
