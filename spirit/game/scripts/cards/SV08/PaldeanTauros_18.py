from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_stage1_pokemon

card = PokemonCardDef(
    guid="f9ea616c-d360-5cb1-92fb-27bef9ad4f2b",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros","Basic","PaldeanTauros"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    family_id=128,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Spirited Tackle",
            game_text="If your opponent's Active Pokémon is a Stage 1 Pokémon, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=bonus_if(active_is(is_stage1_pokemon), 90),
        ),
    ],
)
