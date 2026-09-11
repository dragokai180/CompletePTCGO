from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="f3885f13-5a6b-5870-9765-7276eca370d1",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsDubwool.Name",
    display_name="Hop's Dubwool",
    searchable_by=["Hop's Dubwool", "Stage 1", "HopsDubwool"],
    subtypes=["Stage 1"],
    collector_number=136,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsWooloo.Name",
    family_id=831,
    abilities=[
        Ability(
            title="Defiant Horn",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
