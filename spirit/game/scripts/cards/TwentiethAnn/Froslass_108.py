from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fbf9fe63-7f35-5ec5-851d-9df4a02f6707',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name',
    display_name='Froslass',
    searchable_by=['Froslass', 'Stage 1', 'Froslass'],
    subtypes=['Stage 1'],
    collector_number=108,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    family_id=361,
    abilities=[
        Ability(
            title='Drag Along',
            game_text="If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pokémon is Knocked Out.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pokémon is Knocked Out."),
        ),
        Attack(
            title='Snowy Drop',
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
