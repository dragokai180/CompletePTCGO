from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per

card = PokemonCardDef(
    guid="d1dfb516-cdc6-5691-9c39-9a2e9078bc4a",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoex.Name",
    display_name="Tapu Koko ex",
    searchable_by=["Tapu Koko ex","Basic","ex","TapuKokoex"],
    subtypes=["Basic","ex"],
    collector_number=51,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    family_id=785,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Linked Lightning",
            game_text="This attack does 20 more damage for each of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_bench("mine"), 20, base=60),
        ),
    ],
)
