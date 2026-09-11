from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="956057a9-1cdd-5000-ad2d-4482318986c1",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiant.Name",
    display_name="Iron Valiant",
    searchable_by=["Iron Valiant", "Basic", "Future", "IronValiant"],
    subtypes=["Basic", "Future"],
    collector_number=79,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=1006,
    abilities=[
        Attack(
            title="Gemini Laser",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Zen Blade",
            game_text="During your next turn, this Pokémon can't use Zen Blade.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
