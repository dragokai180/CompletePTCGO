from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import guts_survive_passive
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="56a17587-edc4-59a0-aa22-bae89d912c57",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex","Basic","ex","Pikachuex"],
    subtypes=["Basic","ex"],
    collector_number=57,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    family_id=25,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Resolute Heart",
            game_text="If this Pokémon has full HP and would be Knocked Out by damage from an attack, it is not Knocked Out, and its remaining HP becomes 10.",
            passive=guts_survive_passive(hp_floor=10, flip=False, require_full_hp=True),
        ),
        Attack(
            title="Topaz Bolt",
            game_text="Discard 3 Energy from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1},
            damage=300,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)
