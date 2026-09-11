from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="f511337f-0f06-562f-ad2e-69ee47ec75c2",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricityex.Name",
    display_name="Toxtricity ex",
    searchable_by=["Toxtricity ex", "Stage 1", "ex", "Toxtricityex"],
    subtypes=["Stage 1", "ex"],
    collector_number=215,
    set_code="SVP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Strumming Thunder",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=standard_attack,
        ),
    ],
)
