from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="52c183a9-afbc-5a22-961c-c1bd5e6118d3",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantulaex.Name",
    display_name="Galvantula ex",
    searchable_by=["Galvantula ex", "Stage 1", "Tera", "ex", "Galvantulaex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=51,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Charged Web",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 110 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Fulgurite",
            game_text="Discard all Energy from this Pokémon. During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
