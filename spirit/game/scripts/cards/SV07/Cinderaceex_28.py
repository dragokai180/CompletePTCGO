from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="f3a31e86-66dc-5299-90cc-4b68a8d51b3c",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderaceex.Name",
    display_name="Cinderace ex",
    searchable_by=["Cinderace ex", "Stage 2", "Tera", "ex", "Cinderaceex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=28,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Flare Strike",
            game_text="During your next turn, this Pokémon can't use Flare Strike.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=280,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title="Garnet Volley",
            game_text="This attack does 180 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
