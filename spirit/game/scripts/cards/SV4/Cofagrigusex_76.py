from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe326323-ac98-5c09-a6e0-c4bf4951f791',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigusex.Name',
    display_name='Cofagrigus ex',
    searchable_by=['Cofagrigus ex', 'Stage 1', 'ex', 'Cofagrigusex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=76,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name',
    family_id=562,
    abilities=[
        Ability(
            title='Gold Coffin',
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            passive=standard_passive("If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for a card and put it into your hand. Then, shuffle your deck."),
        ),
        Attack(
            title='Hollow Hands',
            game_text="Put 5 damage counters on your opponent's Benched Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
