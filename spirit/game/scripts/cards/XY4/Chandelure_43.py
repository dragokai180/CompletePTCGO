from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='42875cb6-5f32-56dc-87bb-372f7988be5f',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name',
    display_name='Chandelure',
    searchable_by=['Chandelure', 'Stage 2', 'Chandelure'],
    subtypes=['Stage 2'],
    collector_number=43,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    family_id=607,
    abilities=[
        Ability(
            title='Fainting Spell',
            game_text="If this Pokémon is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pokémon is Knocked Out.",
            passive=standard_passive("If this Pokémon is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pokémon is Knocked Out."),
        ),
        Attack(
            title='Cursed Drop',
            game_text="Put 6 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
