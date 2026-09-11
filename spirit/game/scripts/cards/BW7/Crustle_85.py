from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, self_energy_discard_attack
from spirit.game.card_effects.passives_common import guts_survive_passive

card = PokemonCardDef(
    guid="9a697802-b4c0-5b83-a8eb-ef72192c2406",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle","Stage 1","Crustle"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    abilities=[
        Ability(
            title="Sturdy",
            game_text="If this Pokémon has full HP and would be Knocked Out by damage from an attack, this Pokémon is not Knocked Out and its remaining HP becomes 10 instead.",
            passive=guts_survive_passive(hp_floor=10, flip=False, require_full_hp=True),
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
