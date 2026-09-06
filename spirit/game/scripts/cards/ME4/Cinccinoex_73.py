from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive

card = PokemonCardDef(
    guid="cf282789-0b68-503d-aaf9-08259aac4f21",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccinoex.Name",
    display_name="Cinccino ex",
    searchable_by=["Cinccino ex","Stage 1","ex","Cinccinoex"],
    subtypes=["Stage 1","ex"],
    collector_number=73,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Ability(
            title="Smooth Coat",
            game_text="If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.",
            passive=flip_prevent_damage_passive("Smooth Coat"),
        ),
        Attack(
            title="Energized Slap",
            game_text="This attack does 40 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=damage_per(count_energy("self"), 40),
        ),
    ],
)
