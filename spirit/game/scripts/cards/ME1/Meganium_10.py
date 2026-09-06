from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import Passive, active_passives


class WildGrowthPassive(Passive):
    """Each Basic Grass Energy attached to all of your Pokémon provides
    GrassGrass Energy. Does not stack."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            return options
        if not energy_provides_type(energy, PokemonTypes.GRASS.value):
            return options
        if any(len(option) >= 2 for option in options):
            return options
        active_here = any(
            isinstance(p, WildGrowthPassive) and c.owning_player_id == holder.owning_player_id
            for p, c in active_passives(board)
        )
        if not active_here:
            return options
        return [list(option) * 2 for option in options]


card = PokemonCardDef(
    guid="5dfdddae-27e8-5b5e-8fda-d0956e660044",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium","Stage 2","Meganium"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    family_id=152,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    abilities=[
        Ability(
            title="Wild Growth",
            game_text="Each Basic Grass Energy attached to all of your Pokémon provides GrassGrass Energy. The effect of Wild Growth doesn't stack.",
            passive=WildGrowthPassive(),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
