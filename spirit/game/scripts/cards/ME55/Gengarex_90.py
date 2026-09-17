from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bf7b3f3e-d407-5dd4-8f22-53ecf33704ac',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gengarex.Name',
    display_name='Gengar ex',
    searchable_by=['Gengar ex', 'Stage 2', 'ex', 'Gengarex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=90,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    family_id=94,
    abilities=[
        Ability(
            title='Fainting Spell',
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, flip a coin. If heads, the Attacking Pokémon is Knocked Out.",
            passive=standard_passive("If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, flip a coin. If heads, the Attacking Pokémon is Knocked Out."),
        ),
        Attack(
            title='Chaotic Pain',
            game_text="Place 13 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
