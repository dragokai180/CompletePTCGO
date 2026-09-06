from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, damage_counters_on, damage_per

card = PokemonCardDef(
    guid="45d5f3ea-4855-5ddc-af0b-3e06b35f83ca",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BruteBonnet.Name",
    display_name="Brute Bonnet",
    searchable_by=["Brute Bonnet","Basic","BruteBonnet"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    family_id=986,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Attack(
            title="Poison Spray",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Relentless Punches",
            game_text="This attack does 50 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 50, base=50),
        ),
    ],
)
