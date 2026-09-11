from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="945e48bf-d1e5-5817-86af-efdd34b080f1",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medichamex.Name",
    display_name="Medicham ex",
    searchable_by=["Medicham ex", "Stage 1", "ex", "Medichamex"],
    subtypes=["Stage 1", "ex"],
    collector_number=80,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Chi-Atsu",
            game_text="Put damage counters on your opponent's Active Pokémon until its remaining HP is 50.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title="Yoga Kick",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
